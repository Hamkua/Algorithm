import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n, d, start, end, edge;
    static ArrayList<Point>[] data;
    static int[] result;
    static PriorityQueue<Point> pq = new PriorityQueue<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());

        data = new ArrayList[d + 1];
        for(int i = 0; i < d + 1; i++){
            data[i] = new ArrayList<>();
            data[i].add(new Point(1, i + 1));

        }

        for(int i = 0; i<n; i++){
            st = new StringTokenizer(br.readLine());

            start = Integer.parseInt(st.nextToken());
            end = Integer.parseInt(st.nextToken());
            edge = Integer.parseInt(st.nextToken());

            if(end > d){
                continue;
            }
            data[start].add(new Point(edge, end));

        }

        System.out.println(dijkstra());
    }

    static class Point implements Comparable<Point>{
        int edge;
        int destination;

        public Point(int edge, int destination){
            this.edge = edge;
            this.destination = destination;
        }

        @Override
        public int compareTo(Point p) {
            return this.edge - p.edge;
        }
    }

    public static int dijkstra(){
        result = new int[d + 1];
        Arrays.fill(result, Integer.MAX_VALUE);
        result[0] = 0;

        pq.add(new Point(0, 0));

        while(!pq.isEmpty()){
            Point point = pq.poll();
            int edge = point.edge;
            int destination = point.destination;

            if(destination == d){
                break;
            }

            for(Point next_point : data[destination]){
                int nextEdge = next_point.edge;
                int nextDestination = next_point.destination;

//                System.out.println(nextDestination);
                int newEdge = edge + nextEdge;
                if(result[nextDestination] > newEdge){
                    result[nextDestination] = newEdge;
                    pq.add(new Point(newEdge, nextDestination));
                }
            }
        }

//        for(int i = 0; i < d + 1; i++){
//            System.out.print(result[i] + ", ");
//        }
//        System.out.println();
        return result[d];
    }
}