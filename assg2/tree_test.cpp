
#include "Tree.h"
#include <stdlib.h>
#include <set>

int mainnn() {
	// Code referenced from https://cplusplus.com/reference/cstdlib/rand/
	Tree<int> tree;

	srand (time(NULL));
	std::set<int> integers;

	for (int i = 0; i < 1000; i++) {
		int x = rand();
		integers.emplace(x);
		tree.insert(x);
	}

	tree.print();

	// now search for the inserted integers
	for (int i: integers) {
		if (!tree.search(i)) {
			std::cout << "couldn't find " << i << std::endl;
			return 0;
		}
	}
}




