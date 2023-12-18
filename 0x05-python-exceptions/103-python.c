#!/bin/bash
#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *element;

    if (!PyList_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        element = PyList_GetItem(p, i);
        printf("Element %ld: ", i);
        if (PyBytes_Check(element))
            printf("bytes\n");
        else if (PyFloat_Check(element))
            printf("float\n");
        else if (PyList_Check(element))
            printf("list\n");
        else if (PyTuple_Check(element))
            printf("tuple\n");
        else if (PyLong_Check(element))
            printf("int\n");
        else if (PyUnicode_Check(element))
            printf("str\n");
        else
            printf("%s\n", Py_TYPE(element)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *string;

    if (!PyBytes_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);
    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++)
        printf("%02x ", (unsigned char)string[i]);
    printf("\n");
}

void print_python_float(PyObject *p)
{
    if (!PyFloat_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid Float Object\n");
        return;
    }

    printf("[.] float object info\n");
    printf("  value: %lf\n", PyFloat_AsDouble(p));
}

