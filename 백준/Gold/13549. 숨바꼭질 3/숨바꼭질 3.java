package baekjoon;

import java.util.*;

public class Main {

    static int[] data = new int[100001];
    static boolean[] visited = new boolean[100001];
    static Deque<Node> queue = new LinkedList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        queue.add(new Node(n, 0));
        visited[n] = true;
        while(!queue.isEmpty()){

            Node pop = queue.poll();
            int current_location = pop.getLocation();
            int current_time = pop.getTime();

            if(current_location == m){
                System.out.println(current_time);
                break;
            }

            int tmp = current_location * 2;
            if(0 <= tmp && tmp < 100001){
                if(!visited[tmp]) {
                    visited[tmp] = true;
                    queue.addFirst(new Node(tmp, current_time));
                }
            }
            tmp = current_location + 1;
            if(0 <= tmp && tmp < 100001){
                if(!visited[tmp]) {
                    visited[tmp] = true;
                    queue.add(new Node(tmp, current_time + 1));
                }
            }

            tmp = current_location - 1;
            if(0 <= tmp && tmp < 100001){
                if(!visited[tmp]) {
                    visited[tmp] = true;
                    queue.add(new Node(tmp, current_time + 1));
                }
            }
        }
    }

    static class Node{
        private int location, time;

        public int getLocation() {
            return location;
        }

        public int getTime() {
            return time;
        }

        public Node(int location, int time){
            this.location = location;
            this.time = time;
        }
    }
}



//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//
//
//
//        br.close();
//    }