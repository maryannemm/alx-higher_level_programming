#include <Python.h>

/**
 * print_python_bytes - Print basic info about Python bytes objects
 * @p: PyObject
 */
void print_python_bytes(PyObject *p)
{
    ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    size = Py_SIZE(p);
    str = ((PyBytesObject *)p)->ob_sval;

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    printf("  first %ld bytes: ", size < 10 ? size + 1 : 10);
    for (i = 0; i <= size && i < 10; ++i)
        printf("%02hhx%c", str[i], i == size ? '\n' : ' ');
}

/**
 * print_python_list - Print basic info about Python lists
 * @p: PyObject
 */
void print_python_list(PyObject *p)
{
    ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    size = Py_SIZE(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    for (i = 0; i < size; ++i)
    {
        item = ((PyListObject *)p)->ob_item[i];
        printf("Element %ld: %s\n", i, item->ob_type->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}

