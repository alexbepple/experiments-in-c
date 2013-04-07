#include <stdio.h>
#include <errno.h>
#include "cbehave/cbehave.h"
#include "bar.h"

FEATURE(1, "Bar")
    SCENARIO("The bar is currently at 42")

        GIVEN("A bar")
//Nothing to do
        GIVEN_END

        WHEN("I check it's level")
            int result = bar();
        WHEN_END

        THEN("I expect it to be 42")
            SHOULD_INT_EQUAL(result, 43);
        THEN_END

    SCENARIO_END
FEATURE_END

int main() {
    cbehave_feature strstr_features[] = {
        {feature_idx(1)},
    };

    return cbehave_runner("Bar Features are as belows:", strstr_features);
}
