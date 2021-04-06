from peerQs import MChoice


def test_one():
    m = MChoice(
        "\n\nStep 1: write down the number 0\nStep 2: add 3\nStep 3: return to step 1\n\nIs this an algorithm?",
        0,
        [
            "Yes",
            "No, because it contains an inﬁnite number of steps",
            "No, because it never halts",
            "No, because step 3 is not well-deﬁned",
        ],
    )

    print(m.question)
    print(m)
    assert str(m)[:12] == ".. mchoice::"
    assert str(m) == correct.format(m.id)


correct = """.. mchoice:: {}

    Step 1: write down the number 0
    Step 2: add 3
    Step 3: return to step 1
    
    Is this an algorithm?

    - Yes

      + correct

    - No, because it contains an inﬁnite number of steps

      - incorrect

    - No, because it never halts

      - incorrect

    - No, because step 3 is not well-deﬁned

      - incorrect
"""
