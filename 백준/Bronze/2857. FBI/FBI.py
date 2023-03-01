def find_fbi_agent(agent_list):
    result = "HE GOT AWAY!"
    fbi_agent_ids = []
    for agent_id, agent in enumerate(agent_list):
        if agent.find("FBI") != -1:
            fbi_agent_ids.append(str(agent_id + 1))
    
    if fbi_agent_ids != []:
        result = " ".join(fbi_agent_ids)
    return result

if __name__ == "__main__":
    agent_list = []
    for _ in range(5):
        agent = input()
        agent_list.append(agent)
    print(find_fbi_agent(agent_list))