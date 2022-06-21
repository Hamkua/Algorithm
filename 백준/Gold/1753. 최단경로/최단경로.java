import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    static class Node implements Comparable<Node>{
        private int weight, destination;

        public Node(int weight, int destination){
            this.weight = weight;
            this.destination = destination;
        }

        public int getWeight() {
            return weight;
        }

        public int getDestination() {
            return destination;
        }

        @Override
        public int compareTo(Node o) {
            if(this.getWeight() > o.getWeight()){
                return 1;
            }else{
                return -1;
            }
        }
    }

    static int[] result;
    static PriorityQueue<Node> pq = new PriorityQueue<Node>();
    static LinkedList[] data;

    static int[] dijkstra(int s){
        pq.add(new Node(0, s));
        result[s] = 0;

        while(!pq.isEmpty()){
            Node node = pq.peek();
            pq.remove();

            Iterator it = data[node.getDestination()].iterator();
            while(it.hasNext()){
                Node tmpNode = (Node)it.next();
                int next_weight = tmpNode.getWeight() + node.getWeight();

                if(result[tmpNode.getDestination()] > next_weight){
                    result[tmpNode.getDestination()] = next_weight;
                    pq.add(new Node(next_weight, tmpNode.getDestination()));
                }
            }
        }

        return result;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] strings = br.readLine().split(" ");
        int v = Integer.parseInt(strings[0]);
        int e = Integer.parseInt(strings[1]);


        data = new LinkedList[v + 1];
        for(int i = 0; i<= v; i++){
            data[i] = new LinkedList<Node>();
        }

        result = new int[v + 1];
        for(int i = 0; i<=v; i++ ){
            result[i] = Integer.MAX_VALUE;
        }

        int start = Integer.parseInt(br.readLine());

        for(int i = 0; i<e; i++){
            strings = br.readLine().split(" ");
            int f = Integer.parseInt(strings[0]);
            int t = Integer.parseInt(strings[1]);
            int w = Integer.parseInt(strings[2]);

            data[f].add(new Node(w, t));
        }

        int[] answer = dijkstra(start);
        for(int i = 1; i<=v; i++){
            if(answer[i] == Integer.MAX_VALUE){
                System.out.println("INF");
            }else {
                System.out.println(answer[i]);
            }
        }

        br.close();
    }
}
