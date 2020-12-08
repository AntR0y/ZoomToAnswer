from serpapi import GoogleSearch
import requests
import pyperclip
from Zoom_Control import openChat
def searchQuery(q):
    params = {
      "q": q,
      'location':'Evanston,Illinois',
      "hl": "en",
      "gl": "us",
      "device": "desktop",
      "api_key": "15a037764e46ed48d7f0a90e1608802f1f89e989abb185fa6279192ee7a8d66f"
    }

    client = GoogleSearch(params)
    results = client.get_dict()
    #print(results)
    if 'answer_box' in results:
        res = results['answer_box']
        if 'result' in res:
            output = res['result']
        elif 'snippet' in res:
            output = res['snippet']
        elif 'definition' in res:
            output = res['definition']
        else:
            output = results['answer_box']

        # Check if Question is included in answer -- if so, omit it and include the voice query instead
        output_list = str(output).split('?', 1)
        print(output_list)
        if len(output_list) == 1:
            output = output_list[0]
        else:
            output = output_list[1]

        q_and_a = "------------\nQuestion: " + str(q) + '\n\n' + "Answer: " + str(output)
        pyperclip.copy(q_and_a + '\n------------')
        pyperclip.paste()
    elif 'knowledge_graph' in results:
        res = results['knowledge_graph']
        if 'title' in res:
            output = res['title']
        elif 'snippet' in res:
            output = res['snippet']
        else:
            output = results['knowledge_graph']
        try:
            link = res['link']
        except:
            link = ""

        # Check if Question is included in answer -- if so, omit it and include the voice query instead
        output_list = str(output).split('?', 1)
        print(output_list)

        if len(output_list) == 1:
            output = output_list[0]
        else:
            output = output_list[1]
        
        q_and_a = "------------\nQuestion: " + str(q) + '\n\n' + "Answer: " + str(output)
        pyperclip.copy(q_and_a + '\n' + str(link) + '------------')
        pyperclip.paste()
    else:
        print('links')
        found = False
        links = ''
        output = ''
        for i in results:
            if type(results[i]) == list:
                for k in range(len(results[i])):
                    if 'snippet' in results[i][k]:
                        output = results[i][k]['snippet'] + '  LINK AT:' + results[i][k]['link']
                        found = True
                        links = getLinks(results[i])
                        break
                if found:
                    break
        if not found:
            output = "NO VALID ANSWERS"

        # Check if Question is included in answer -- if so, omit it and include the voice query instead
        output_list = str(output).split('?', 1)
        print(output_list)

        if len(output_list) == 1:
            output = output_list[0]
        else:
            output = output_list[1]

        q_and_a = "------------\nQuestion: " + str(q) + '\n\n' + "Answer: " + str(output)
        pyperclip.copy(q_and_a + '\n \n' + links + '------------')
        pyperclip.paste()

    openChat()

def getLinks(my_list):
    links = ''
    for k in range(0, min(6, len(my_list))):
        links += str(k+1) + ')' +my_list[k]['link'] + '\n'
    return links


#searchQuery("what is the integral of sinx")
"""
    elif 'top_stories' in results:
        output = ""
        res = results['top_stories']
        if 'title' in res:
            output = res['title']
        pyperclip.copy(str(output))
        pyperclip.paste()
"""