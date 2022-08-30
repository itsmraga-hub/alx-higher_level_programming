#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints list info in python
 *
 * @p: PyObject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	long int s, i;
	PyListObject *list;
	PyObject *item;

	s = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", s);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < s; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
