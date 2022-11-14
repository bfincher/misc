#pragma once

#include <iostream>
#include <string>
#include <list>
#include <vector>

class Card {
private:
	int index;
	std::string keyword;

public:
	Card(int index, std::string keyword);

	Card(const Card &other);

	~Card();

	int getIndex() const;

	std::string getKeyword() const;

	Card& operator=(const Card &other);

	bool operator==(const Card &other) const;

	bool operator<(const Card &other) const;

	bool operator>(const Card &other) const;

	friend std::ostream& operator<<(std::ostream &os, const Card &dt) {
		os << dt.index << " -> " << dt.keyword;
		return os;
	}
};

class IndexCards {
private:
	std::list<Card> cardsByIndex;
	std::list<Card> cardsByKeyword;

	void insertByIndex(Card card);
	void insertByKeyword(Card card);
	void print(std::list<Card> theList);
	std::vector<Card> toVector(std::list<Card> theList);
	void removeCard(std::list<Card> &cards, Card card);

public:
	IndexCards();

	IndexCards(const IndexCards &other);

	~IndexCards();

	IndexCards& operator=(const IndexCards &other);

	void insert(Card card);

	void printByIndex();

	void printByKeyword();

	std::vector<Card> getByIndex();

	std::vector<Card> getByKeyword();

	void removeCard(Card card);

};
