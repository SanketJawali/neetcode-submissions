class Solution {
    HashMap<Integer, Integer> count = new HashMap();

    public void sortColors(int[] nums) {
        count.put(0, 0);
        count.put(1, 0);
        count.put(2, 0);

        // Count each color
        for (int n: nums) {
            count.put(n, count.get(n) + 1);
        }
        // Refill nums with colors in order 0, 1, 2, with counts as their frequency
        for (int i = 0; i < count.get(0); i++) {
            nums[i] = 0;
        }
        int offset = count.get(0);
        for (int i = 0; i < count.get(1); i++) {
            nums[i + offset] = 1;
        }
        offset += count.get(1);
        for (int i = 0; i < count.get(2); i++) {
            nums[i + offset] = 2;
        }
    }
}