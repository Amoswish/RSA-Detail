# include <stdio.h>
# include <stdlib.h>
  typedef long long ll;
  ll ModMul(ll a,ll b,ll n)//快速积取模 a*b%n
  {
      ll ans=0;
      while(b)
      {
          if(b&1)
            ans=(ans+a)%n;
          a=(a+a)%n;
          b>>=1;
      }
      return ans;
  }
  ll ModExp(ll a,ll b,ll n)//快速幂取模 a^b%n
  {
      ll ans=1;
      while(b)
      {
          if(b&1)
            ans=ModMul(ans,a,n);
          a=ModMul(a,a,n);
          b>>=1;
      }
      return ans;
  }
  bool miller_rabin(ll n)//Miller-Rabin素数检测算法
  {
      ll i,j,a,x,y,t,u,s=10;
      if(n==2)
        return true;
      if(n<2||!(n&1))
        return false;
      for(t=0,u=n-1;!(u&1);t++,u>>=1);//n-1=u*2^t
      for(i=0;i<s;i++)
      {
          a=rand()%(n-1)+1;
          x=ModExp(a,u,n);
          for(j=0;j<t;j++)
          {
              y=ModMul(x,x,n);
              if(y==1&&x!=1&&x!=n-1)
                return false;
              x=y;
          }
          if(x!=1)
            return false;
      }
      return true;
  }
  int main()
  {
      ll n;
      while(scanf("%lld",&n)!=EOF)
        if(miller_rabin(n))
          printf("Yes\n");
        else
          printf("No\n");
      return 0;
  }
