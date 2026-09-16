class Solution {
    int MOD=1e9+7;
    // cnt  - Number of segments still needed to draw
    long long solve(int n, int k, int i, int cnt, bool flag, vector<vector<vector<long long>>> &dp){
        if(cnt==0)return 1;
        if(i==n)return 0;
        if(dp[i][cnt][flag]!=-1)return dp[i][cnt][flag];
        long long ans=0;
        // If flag==false: not currently drawing a segment
        // Else, currently drawing a segment
        if(!flag){
            // skip point i, don't start any segment here
            ans=(ans+solve(n,k,i+1,cnt,false,dp))%MOD;
            // start a new segment from point i
            ans=(ans+solve(n,k,i+1,cnt,true,dp))%MOD;
        }
        else{
            // extend segment to next point
            ans=(ans+solve(n,k,i+1,cnt,true,dp))%MOD;
            // end segment at point i, move to position i with one less segment needed
            ans=(ans+solve(n,k,i,cnt-1,false,dp))%MOD;
        }
        return dp[i][cnt][flag]=ans;
    }
public:
    int numberOfSets(int n, int k) {
        // dp[position][segments_remaining][is_drawing]
        vector<vector<vector<long long>>> dp(n+1,vector<vector<long long>>(k+1,vector<long long>(2,-1)));

        return solve(n,k,0,k,false,dp);
    }
};