#include "organizing_list.h"
#include <string>

using namespace std;

int mainn() {
	SelfOrganizingList<string> lst;

	lst.push_back("a");
	lst.push_back("b");
	lst.push_back("c");
	lst.push_back("d");
	lst.print();
	cout << endl << endl;

	lst.moveToFront("c");
	lst.print();
	cout << endl << endl;

	lst.moveToFront("d");
	lst.print();
}



