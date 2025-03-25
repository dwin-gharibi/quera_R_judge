import unittest
import os
from scripts.docker_handler import DockerHandler
from scripts.r_runner import RRunner

class TestRPrograms(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        DockerHandler.start_container()

    # @classmethod
    # def tearDownClass(cls):
    #     DockerHandler.stop_container()

    def test_1(self):
        r_file = "code.r"
        input_file = "input4.txt"
        output_file = "output4.txt"

        RRunner.compile_R(r_file)
        output = RRunner.run_R(r_file, input_file)

        output_path = os.path.join(RRunner.TEST_CASES_FOLDER, "out", output_file)
        with open(output_path, "r") as f:
            expected_output = [line.strip() for line in f.readlines()]

        self.assertEqual(output, expected_output, f"Unexpected output for {r_file}")


if __name__ == "__main__":
    unittest.main()
