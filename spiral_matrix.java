class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<Integer>();
        if(matrix.length == 0) return result;
        int down = 0, right = 0; 
        boolean upB = false, downB = false, leftB = false, rightB = true;
        result.add(matrix[0][0]);
        int maxRight = matrix[0].length-1, maxLeft = 0;
        int maxUp = 1, maxDown = matrix.length- 1;
        
        
        while(result.size() != matrix.length*matrix[0].length){        
           if(rightB){ 
                if(right == maxRight){
                    rightB = false;
                    downB = true;
                    maxRight--;
                    down++;
                }else{ right++; }   
            }
           else if(leftB){ 
                if(right == maxLeft){
                   leftB = false; 
                   upB = true;
                    maxLeft++;
                    down--;
                }else{ right--;}
            }
           else if(upB){
                if(down == maxUp){
                   upB = false; 
                   rightB = true;
                   maxUp++;
                   right++;
                }else{ down--; }
            }
           else if(downB){
                if(down == maxDown){
                   downB = false; 
                   leftB = true;
                   maxDown--;
                   right--; 
                }else{ down++; }
                
            }
            result.add(matrix[0+down][0+right]);
                
        }
        
        return result;  
    }
}
