def encoding(value):
    result = []
    final_result = []
    last_result = ""
    for n in value:
        resul = f"{n}{value.count(n)}"

    
        result.append(resul)
        # " ".join(result)
  
    final_result = list(dict.fromkeys(result))

    last_result = "".join(final_result)
    
    print(last_result)

encoding("abbaa")