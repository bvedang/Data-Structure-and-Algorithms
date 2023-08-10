class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        HashMap<Integer, Integer> comp = new HashMap<>();
        for(int i=0;i< nums.length;i++){
            int complement = target - nums[i];
            if(comp.containsKey(complement)){
                res[0] = i;
                res[1] = comp.get(complement);
                break;
            }
            else{
                comp.put(nums[i],i);
            }
        }
        return res;
        
    }
}