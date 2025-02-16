# NOTE: Generated By HttpRunner v3.1.4
# FROM: request_methods/request_with_functions.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseRequestWithRetry(HttpRunner):

    config = (
        Config("request methods testcase with retry")
        .variables(
            **{
                "foo1": "config_bar1",
                "foo2": "config_bar2",
                "expect_foo1": "config_bar1",
                "expect_foo2": "config_bar2",
                "sum_v": 0
            }
        )
        .base_url("https://postman-echo.com")
        .verify(False)
        .export(*["foo3"])
        .locust_weight(2)
    )

    teststeps = [
        Step(
            RunRequest("get with params and retry 3 times")
            .retry_on_failure(3, 0.5)
            .with_variables(
                **{"foo1": "bar11", "foo2": "bar21"}
            )
            .get("/get")
            .with_params(**{"foo1": "$foo1", "foo2": "$foo2", "sum_v": "${sum_two($sum_v, 1)}"})
            .with_headers(**{"User-Agent": "HttpRunner/${get_httprunner_version()}"})
            .extract()
            .with_jmespath("body.args.foo2", "foo3")
            .with_jmespath("body.args.sum_v", "sum_v")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.args.foo1", "bar11")
            .assert_equal("body.args.sum_v", "4")
            .assert_equal("body.args.foo2", "bar21")
        )
    ]


if __name__ == "__main__":
    TestCaseRequestWithRetry().test_start()
