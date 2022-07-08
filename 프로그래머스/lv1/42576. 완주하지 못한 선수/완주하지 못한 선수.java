import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String, Integer> map = new HashMap<String, Integer>();
        for(int i = 0; i<participant.length; i++){
            if(map.containsKey(participant[i])){
                int count = map.get(participant[i]);
                map.put(participant[i], ++count);
                
            }
            else{
                map.put(participant[i],1);
            }
        }
        for(String i:completion){
            int count = map.get(i);
            map.put(i,--count);
            if(map.get(i) == 0){
                map.remove(i);
            }
        }
        for(String j:participant){
            if(map.containsKey(j)){
                answer += (j);
                map.remove(j);
            }
        }
        return answer;
    }
}