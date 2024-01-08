#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - prints info about python lists
 * @p: address of pyobject struct
 */
void print_python_list_info(PyObject *p)
{
	int j;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (j = 0; j < Py_SIZE(p); j++)
		printf("Element %d: %s\n", j, Py_TYPE(PyList_GetItem(p, j))->tp_name);
}
