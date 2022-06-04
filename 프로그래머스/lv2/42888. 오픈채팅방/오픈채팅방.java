import java.util.*;
class Solution {
    public static String[] solution(String[] record) {
        String[] answer = {};
        Map<String, String> dic = new HashMap<String, String>();

        int changeCnt = 0;
        int index = 0;

        for(String records: record){
            String[] recordArr = records.split(" ");
            if(recordArr[0].equals("Change") || recordArr[0].equals("Enter")){
                if(recordArr[0].equals("Change")){
                    changeCnt++;
                }
                dic.put(recordArr[1], recordArr[2]);
            }
        }

        answer = new String[record.length - changeCnt];

        for(String records: record){
            String[] recordArr = records.split(" ");

            if(recordArr[0].equals("Leave")){
                answer[index] = dic.get(recordArr[1]) + "님이 나갔습니다.";

            } else if(recordArr[0].equals("Enter")){
                answer[index] = dic.get(recordArr[1]) + "님이 들어왔습니다.";
            } else{
                continue;
            }
            index++;
        }

        return answer;
    }
}