class Solution {
public:

    
    
    string longestPalindrome(string s) {
        string longest ="";
        int a = 0;
        int b; 
        int length = s.length();
        string substr;
        while(a<length){
            substr = "";
            b = 0;
            while(a+b<length){ 
                substr += s[a+b];
                if(b+1 <= longest.length()){ b++; continue;}
                
                bool palin = true;
                int j = 0;
                for(int i=b; i>=0; i--){
                   if(substr[j] != substr[i]){ palin = false; break;}
                   j++;
                 }
                
                if(palin) longest = substr;
                b++;
            }
            a++;
        }
        
        
        
        return longest;
    }
    

};
