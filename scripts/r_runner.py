import os
from scripts.docker_handler import DockerHandler

class RRunner:
    SOLUTION_FOLDER = os.path.abspath("solution")
    TEST_CASES_FOLDER = os.path.abspath("test_cases")
    DOCKER_EXEC = ["docker-compose", "exec", "-T", "octave-container"]

    @staticmethod
    def compile_R(asm_file):
        # No compile needed for @R
        pass

    @staticmethod
    def run_R(r_file, input_file):
        input_path = f"/test_cases/in/{input_file}"
        
        with open(os.path.join(RRunner.TEST_CASES_FOLDER, "in", input_file), "r") as f:
            expected_input = "\n".join([line.strip() for line in f.readlines()])

        command = RRunner.DOCKER_EXEC + ["bash", "-c", f"echo \"{expected_input}\" | Rscript {r_file}"]
        output, _ = DockerHandler.exec_command(command)
        return output
