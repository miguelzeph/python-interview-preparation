
def top_ip(logs:list) -> str | None:
    
    if isinstance(logs,list):
        
        # Counting
        dict_ = {}
        for log in logs:
            ip = log.split("-")[0].strip()
            
            if ip not in dict_:
                dict_[ip] = 1
            
            else:
                dict_[ip] += 1
        
        # Get top ip
        # dict_top_ip = {"ip":None, "count":0}
        # for key, value in dict_.items():
        #     if dict_top_ip["count"] < value:
                
        #         dict_top_ip["count"] = value
        #         dict_top_ip["ip"] = key
                
        # return dict_top_ip["ip"]
        
        return max(dict_, key = dict_.get)
    
        # P.S. In case of draw, we could return a list
        # top_ips = [ip for ip, count in dict_.items() if count == max_count]
        # return top_ips if top_ips else None
    
    return None
        
  


def get_ips():
    
    logs = [
        "10.0.0.1 - user A", 
        "10.0.0.1 - user A",
        "10.0.0.2 - user B",
    ]
    
    return logs

if __name__ == "__main__":
    
    ips = get_ips()
    
    result = top_ip(ips)
    
    if result == "10.0.0.1":
        print("Approved")
    
    else:
        print("Failed")
