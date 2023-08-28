#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_list(PyObject *p)
{
    long int size, i;
    PyListObject *list = (PyListObject *)p;
    const char *type;

    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);
    for (i = 0; i < size; i++)
    {
        type = (list->ob_item[i])->ob_type->tp_name;
        printf("Element %ld: %s\n", i, type);
        if (strcmp(type, "bytes") == 0)
            print_python_bytes(list->ob_item[i]);
        else if (strcmp(type, "float") == 0)
            print_python_float(list->ob_item[i]);
    }
}

void print_python_bytes(PyObject *p)
{
    long int size, i;
    PyBytesObject *bytes = (PyBytesObject *)p;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = bytes->ob_sval;
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    if (size > 10)
        size = 10;
    else
        size++;
    printf("  first %ld bytes:", size);
    for (i = 0; i < size; i++)
        printf(" %02x", str[i] & 0xff);
    printf("\n");
}

void print_python_float(PyObject *p)
{
    double value;
    char *str;

    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    value = ((PyFloatObject *)p)->ob_fval;
    str = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", str);
}
