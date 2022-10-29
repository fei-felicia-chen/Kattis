import java.util.*;

public class breakingbad {

    static boolean dfs(String ingredient) {
        if (!walter.contains(ingredient) && !jesse.contains(ingredient)) {
            walter.add(ingredient);
        }

        // Get items that cannot be together with ingredient and move accordingly
        for (String ing : myMap.get(ingredient)) {
            boolean notAnywhere = !walter.contains(ing) && !jesse.contains(ing);
            if (walter.contains(ingredient) && notAnywhere) {
                jesse.add(ing);
                dfs(ing);
            } else if (jesse.contains(ingredient) && notAnywhere) {
                walter.add(ing);
                dfs(ing);
            } else if ((jesse.contains(ingredient) && jesse.contains(ing)) ||
                       (walter.contains(ingredient) && walter.contains(ing))) {
                return false;
            }
        }
        return true;
    }

    static HashMap<String, Set<String>> myMap; // map of {ingredient : set(sus ingredients)}
    static Set<String> walter, jesse;
    static Set<String> allIngredients;
    static boolean good;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        myMap = new HashMap<>();
        walter = new HashSet<>();
        jesse = new HashSet<>();
        good = true;
        allIngredients = new HashSet<>();

        // Get all ingredients, add to all ingredients and initialize set for map
        for (int i = 0; i < N; i++) {
            String s = sc.next();
            allIngredients.add(s);
            myMap.put(s, new HashSet<>());
        }

        // Add sus ingredients to map's values
        int M = sc.nextInt();
        for (int i = 0; i < M; i++) {
            String ing1 = sc.next();
            String ing2 = sc.next();
            myMap.get(ing1).add(ing2);
            myMap.get(ing2).add(ing1);
        }

        // Separate lists using DFS
        for (String s : allIngredients) {
            if (!dfs(s))
            {
                good = false;
                System.out.println("impossible");
                break;
            }   
        }

        if (good) {
            for (String s : walter) {
                System.out.print(s + " ");
            }
            System.out.print("\n");
            for (String s : jesse) {
                System.out.print(s + " ");
            }
        }
        sc.close();
    }
}
