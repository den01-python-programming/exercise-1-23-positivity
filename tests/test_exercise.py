import pytest
import src.exercise

def test_exercise():
    input_values = ["2","-150","0"]
    input_values_stored = ["2","-150","0"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert [output[0],output[1],output[2],output[3],output[4],output[5]] == ["Give a number:","The number is positive.",\
                                               "Give a number:","The number is not positive.",\
                                               "Give a number:","The number is not positive."]
