class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
      
        HashMap<String, Integer> andy = new HashMap<String, Integer>();
        HashMap<String, Integer> common = new HashMap<String, Integer>();
        List<String> result = new ArrayList<String>();
        int least = 10000;
        for(int a=0; a<list1.length; a++){
            andy.put(list1[a], a);
        }
        
        for(int a=0; a<list2.length; a++){
            if(andy.get(list2[a]) == null) continue;
            else{ 
                common.put(list2[a], a+andy.get(list2[a]));
                if(least > common.get(list2[a])) least = common.get(list2[a]);
                }
        }
        
        for(String i : common.keySet()){
           if(common.get(i) == least){ result.add(i);}
        }
        
       String[] sresult = new String[result.size()];
        
       for(int a=0; a<result.size(); a++){
           sresult[a] = result.get(a);
       } 
        
        return sresult;
        
    }
}
