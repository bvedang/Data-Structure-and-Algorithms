class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer,Integer> comp = new HashMap<Integer, Integer>();
        for(int i = 0;i<nums.length;i++){
            if(comp.containsKey(nums[i])){
                return true;
            }
            else{
                comp.put(nums[i],i);
            }
        }
        return false;
    }
}