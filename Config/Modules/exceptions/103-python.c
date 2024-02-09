#include <Python.h>
#include <stdio.h>

/**
 * Author: Tafara-N
 *
 * Description: Three C functions that print some basic info about Python lists,
 *										Python bytes an Python float objects.
 */

/*-----------------------------------------------------------------------------*/


/**
 * print_python_float - Data for the PyFloatObject
 * @p: PyFloatObject
 */

void print_python_float(PyObject *p)
{
	double value = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	value = ((PyFloatObject *)p)->ob_fval;
	string = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", string);
}

/**
 * print_python_bytes - Data for the PyBytesObject
 * @p: PyBytesObject
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, x = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	string = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);

	while (x < size + 1 && x < 10)
	{
		printf(" %02hhx", string[x]);
		x++;
	}
	printf("\n");
}

/**
 * print_python_list - Data for the PyListObject
 * @p: PyListObject
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *y;
	int x = 0;

	fflush(stdout);
	printf("[*] Python list info\n");

	if (PyList_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		while (x < size)
		{
			y = PyList_GET_ITEM(p, x);
			printf("Element %d: %s\n", x, y->ob_type->tp_name);

			if (PyBytes_Check(y))
				print_python_bytes(y);

			else if (PyFloat_Check(y))
				print_python_float(y);
			x++;
		}
	}

	else
		printf("  [ERROR] Invalid List Object\n");
}

