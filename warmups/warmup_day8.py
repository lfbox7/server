#!/usr/bin/python3

quiz= {
    "1":{
        "question": "Aye you a horse?",
        "yes": "2",
        "no":"end"
    },
    "2":{
        "question": "Do you walk on four legs?",
        "yes": "3",
        "no": "end"
    },
    "3":{
        "question": "Really?",
        "yes": "4",
        "no": "end"
    },
    "4":{
        "question": "Can you read and write?",
        "yes": "end",
        "no": "5"
    },
    "5":{
        "question": "Liar, you're reading this.",
        "yes": "end",
        "no": "end"
    },
    "end":{
        "question": "You're not a horse.",
    }
}
print('Please answer [yes] or [no].\n')

for i in range(1,6):

    print(quiz[str(i)].get('question'))
    choice = input('> ').lower()
    while choice.lower() not in {'no', 'yes'}:
        print(quiz[str(i)].get('question'))
        choice = input('> ').lower()

    ans = quiz[str(i)].get(choice)
    if ans.isnumeric():
        i = int(ans)
    else:
        break

print(f"\n{quiz['end'].get('question')}")
