class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int[] left = {3,0};
        int[] right = {3,2};
        int mid;

        for(int i=0; i<numbers.length; i++){
            if((numbers[i] % 3) == 1){
                answer += 'L';
                left[0] = numbers[i] / 3;
                left[1] = 0;
            }
            else if(((numbers[i] % 3) == 0) && (numbers[i] != 0)){
                answer += 'R';
                right[0] = numbers[i] / 4;
                right[1] = 2;
            }
            else{
                if(numbers[i] == 0){
                    mid = 3;
                } else{
                    mid = numbers[i] / 3;
                }
                if((Math.abs(mid - right[0]) + Math.abs(right[1] - 1)) > Math.abs(mid - left[0])+ Math.abs(left[1] - 1)){
                    answer += 'L';
                    left[0] = mid;
                    left[1] = 1;
                } else if((Math.abs(mid - right[0]) + Math.abs(right[1] - 1)) < Math.abs(mid - left[0])+ Math.abs(left[1] - 1)){
                    answer += 'R';
                    right[0] = mid;
                    right[1] = 1;
                } else{
                    if(hand.equals("right")){
                        answer += 'R';
                        right[0] = mid;
                        right[1] = 1;
                    } else{
                        answer += 'L';
                        left[0] = mid;
                        left[1] = 1;
                    }
                }
            }

        }
        return answer;
    }
}