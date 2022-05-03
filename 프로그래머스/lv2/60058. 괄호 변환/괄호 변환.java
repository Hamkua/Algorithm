import java.util.LinkedList;
import java.util.Queue;
class Solution {
    public boolean check(String p){
        Queue<Character> queue = new LinkedList<>();
        int balance = 0;
        for(int i = 0; i<p.length(); i++){
            if(p.charAt(i) == '('){
                queue.add(p.charAt(i));
                balance++;
            } else{
                if(queue.isEmpty()){
                    return false;
                }
                balance--;
                queue.poll();
            }
        }
        if(balance != 0) {
            return false;
        }
        return true;
    }
    
    public String solution(String p) {
        String answer = "";
        int divIndex = 0;
        int balance = 0;
        for(int i =0; i<p.length(); i++){
            if(p.charAt(i) == '('){
                balance++;
            } else{
                balance--;
            }

            if(balance == 0){
                divIndex = i;
                break;
            }
        }
        String u,v;
        if(divIndex != 0) {
            u = p.substring(0, divIndex + 1);
            v = p.substring(divIndex + 1);
        } else{
            return "";
        }
        boolean isPerfect = check(u);
        if(isPerfect){
            answer = u + solution(v);
        } else{
            String tmp =  "(" + solution(v) + ")";

            if(u.length() > 2) {
                u = u.substring(1, u.length() - 1);
                for(int i = 0; i< u.length(); i++){
                    if(u.charAt(i) == '('){
                        u = u.substring(0,i) + ")" + u.substring(i+1);
                    } else{
                        u = u.substring(0,i) + "(" + u.substring(i+1);
                    }
                }
            } else{
                u = "";
            }
            answer = tmp + u;
        }
        return answer;
    }
}