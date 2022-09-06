#pragma once

#include <iostream>
#include <string>
#include <list>

class Card {
private:
	int index;
	std::string keyword;

public:
	Card(int index, std::string keyword) :
			index(index), keyword(keyword) {
	}

	Card(const Card &other) :
			index(other.index), keyword(other.keyword) {
	}

	~Card() {
	}

	Card& operator=(const Card &other) {
		index = other.index;
		keyword = other.keyword;
		return *this;
	}

	bool operator==(const Card &other) const {
		return index == other.index && keyword == other.keyword;
	}

	bool operator<(const Card &other) const {
		return index < other.index;
	}

	bool operator>(const Card &other) const {
		return index > other.index;
	}

	friend std::ostream& operator<<(std::ostream &os, const Card &dt) {
		os << dt.index << " -> " << dt.keyword;
		return os;
	}
};

class IndexCards {
private:
	std::list<Card> cards;

public:
	IndexCards() {
	}

	IndexCards(const IndexCards &other) :
			cards(other.cards) {
	}

	~IndexCards() {
	}

	IndexCards& operator=(const IndexCards &other) {
		cards = other.cards;
		return *this;
	}

	void insert(Card card) {
		for (auto itr = cards.begin(); itr != cards.end(); itr++) {
			if (card < *itr) {
				cards.insert(itr, card);
				return;
			}
		}

		cards.push_back(card);
	}

	void print() {
		for (auto itr = cards.begin(); itr != cards.end(); itr++) {
			std::cout << *itr << std::endl;
		}
	}

};
