#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_string - Prints Python string information
 * @p: PyObject string
 */
void print_python_string(PyObject *p)
{
    PyCompactUnicodeObject *unicode;
    PyASCIIObject *ascii;

    printf("[.] string object info\n");

    if (PyUnicode_Check(p))
    {
        unicode = (PyCompactUnicodeObject *)p;
        printf("  type: compact unicode object\n");
        printf("  length: %lu\n", PyUnicode_GET_LENGTH(unicode));
        printf("  value: %ls\n", PyUnicode_AS_UNICODE(unicode));
    }
    else if (PyBytes_Check(p))
    {
        ascii = (PyASCIIObject *)p;
        printf("  type: compact ascii\n");
        printf("  length: %lu\n", ascii->length);
        printf("  value: %s\n", PyBytes_AS_STRING(p));
    }
    else
    {
        printf("  [ERROR] Invalid String Object\n");
    }
}

