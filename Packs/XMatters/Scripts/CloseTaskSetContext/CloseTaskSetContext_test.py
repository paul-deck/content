# Test runner for CloseTaskSetContext

import demistomock as demisto
from CloseTaskSetContext import main


def test_close_task_set_context(mocker):
    demisto.log("stuff")

    def executeCommand(name, args=None):
        if name == "taskComplete":
            # Success
            return {}
        else:
            raise ValueError(f"Unimplemented command called: {name}")

    mocker.patch.object(
        demisto,
        "args",
        return_value={"entry_id": "waiter", "context_key": "XMatters.UserResponseOut", "comments": "This is a comment"},
    )

    # mocker.patch.object(demisto, 'executeCommand', side_effect=executeCommand)
    mocker.patch.object(demisto, "results")

    main()

    # If we got here we're good.
    assert True
