class utilities:
    @staticmethod
    def verify_string_text(Expected, Actual):
        expected_value = Expected.strip()
        actual_value = Actual.strip()

        if ":" in actual_value:
            actual_value = actual_value.split(":", 1)[1].strip()

        assert expected_value == actual_value, f"Validation failed. Expected: {expected_value}, Actual: {actual_value}"
        print(f"Expected: {expected_value} , Actual: {actual_value}")

