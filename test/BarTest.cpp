#include "gtest/gtest.h"
#include "Bar.h"

TEST(Bar, findsTheTruth) {
	EXPECT_EQ(42, bar());
}
