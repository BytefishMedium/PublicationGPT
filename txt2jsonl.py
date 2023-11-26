import json

# read data from startup.txt, toward_data_science.txt, better_programming.txt , save them in list
def read_txt():
    with open('startup.txt', 'r', encoding='utf-8') as f:
        startup = f.readlines()
    with open('toward_data_science.txt', 'r', encoding='utf-8') as f:
        toward_data_science = f.readlines()
    with open('better_programming.txt', 'r', encoding='utf-8') as f:
        better_programming = f.readlines()
    return startup, toward_data_science, better_programming

system_content = "After I give you a title, guess which publication it belongs to. "

if __name__ == '__main__':
    startup, toward_data_science, better_programming = read_txt()

    # format：{"messages": [{"role": "system", "content": ""}, {"role": "user", "content": "What's the capital of France?"}, {"role": "assistant", "content": "Paris, as if everyone doesn't know that already."}]}

    list = []

    for i in range(len(startup)):
        list.append({"messages": [{"role": "system", "content": system_content}, {"role": "user", "content": startup[i]}, {"role": "assistant", "content": "startup"}]})

    for i in range(len(toward_data_science)):
        list.append({"messages": [{"role": "system", "content": system_content}, {"role": "user", "content": toward_data_science[i]}, {"role": "assistant", "content": "toward_data_science"}]})

    for i in range(len(better_programming)):
        list.append({"messages": [{"role": "system", "content": system_content}, {"role": "user", "content": better_programming[i]}, {"role": "assistant", "content": "better_programming"}]})
    print(list)

    # turn list into jsonl file
    with open('data.jsonl', 'w', encoding='utf-8') as f:
        for i in range(len(list)):
            f.write(json.dumps(list[i], ensure_ascii=False) + '\n')