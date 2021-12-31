from taskcat.testing import CFNTest


def test_topic():
    test = CFNTest.from_file(input_file='./.taskcat.yml')
    output_dict = {}
    with test as stacks:
        # Calling 'with' or 'test.run()' will deploy the stacks.
        for stack in stacks:
            print(f"Testing {stack.name}")
            topic_name = ""
            for output in stack.outputs:
                output_dict[output.key] = output.value
            assert "WebsiteURL" in output_dict
