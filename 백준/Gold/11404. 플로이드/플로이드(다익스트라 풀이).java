import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static ArrayList<Point>[] data;
    static int[] result;
    static PriorityQueue<Point> pq;
    static StringTokenizer st;
    static int n, m, start, end, edge;

    static final int INF = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        data = new ArrayList[n + 1];
        for(int i = 0; i <n +1; i++){
            data[i] = new ArrayList<>();
        }


        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            start = Integer.parseInt(st.nextToken());
            end = Integer.parseInt(st.nextToken());
            edge = Integer.parseInt(st.nextToken());

            data[start].add(new Point(edge, end));
        }

        for(int i = 1; i < n + 1; i++){
            dijkstra(i);
        }


    }

    static int[] dijkstra(int from){
        result = new int[n + 1];
        Arrays.fill(result, INF);
        pq = new PriorityQueue<>();
        pq.add(new Point(0, from));
        result[from] = 0;

        while(!pq.isEmpty()){
            Point point = pq.poll();
            int edge = point.edge;
            int destination = point.destination;

            for(Point nextPoint : data[destination]){
                int nextEdge = nextPoint.edge;
                int nextDestination = nextPoint.destination;

                int newEdge = nextEdge + edge;
                if(result[nextDestination] > newEdge){
                    result[nextDestination] = newEdge;
                    pq.add(new Point(newEdge, nextDestination));
                }
            }
        }

        for(int i = 1; i < n + 1; i++){
            if(result[i] == INF){
                System.out.print("0 ");
                continue;
            }
            System.out.print(result[i] + " ");
        }
        System.out.println();

        return result;
    }

    static class Point implements Comparable<Point>{
        int destination;
        int edge;

        public Point(int edge, int destination){
            this.edge = edge;
            this.destination = destination;
        }

        @Override
        public int compareTo(Point p) {
            return this.edge - p.edge;
        }
    }
}


