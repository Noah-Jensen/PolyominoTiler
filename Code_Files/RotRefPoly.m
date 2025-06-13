function SymList = RotRefPoly(P)
%SymList = RotRefPoly(P)
%   Detailed explanation goes here

debug = false;

%Resize PolyMat to be safe
% H = find(any(P));
% V = find(any(P,2));

%Hlen = max(H) - min(H) + 1;
%Vlen = max(V) - min(V) + 1;

PP = P;

P(:,all(~P,1)) = [];
P(all(~P,2),:)= []; 
%P = PP(V(1):V(end),H(1):H(end));

dimens = [size(P,1) size(P, 2)];

PH1 = zeros(dimens(1),dimens(2),4);
PH2 = zeros(dimens(2),dimens(1),4);

PH1(:,:,1) = P;
PH1(:,:,2) = rot90(P,2);
PH1(:,:,3) = rot90(P');
PH1(:,:,4) = rot90(P',-1);

PH2(:,:,1) = rot90(P);
PH2(:,:,2) = rot90(P,-1);
PH2(:,:,3) = P';
PH2(:,:,4) = rot90(P',2);


if (dimens(1)==dimens(2))

Placeholder = zeros(dimens(1),dimens(2),8);

Placeholder(:,:,1:4) = PH1;
Placeholder(:,:,5:8) = PH2;

for j = 1 : 7

    Inset = false(1,8);

    loc = false(1,8 - j);
    
        for i = j : 7
        
            loc(i-j+1) = isequal(Placeholder(:,:,j),Placeholder(:,:,i+1));
        
        end
    
    Inset( j + 1 : 8 ) = loc;

    tempLog = find ( Inset );

    if (debug)
    
        disp('remove duplicates')

    end

    Placeholder(:,:,tempLog) = zeros(dimens(1),dimens(1),length(tempLog));
    
    Sloc = find( sum( sum( Placeholder(:,:,(j:end)), 1 ), 2 ) );
    
    LSloc = length(Sloc);

    if (debug)

    disp('consolidate')

    end

    Placeholder(:,:,j:(j+(LSloc-1))) = Placeholder(:,:,(Sloc + (j-1)));

    if (debug)

    disp('zeros')

    end

    Placeholder(:,:,(j+LSloc):end) = zeros(dimens(1),dimens(1),9-(j+LSloc));


tripSum = sum(sum(sum(Placeholder(:,:,(j+1):end),1),2),3) == zeros(1,8-j);

if ((isequal(Placeholder(:,:,j+1),zeros(dimens(1)))) && (isequal(tripSum,true(1,length(tripSum)))))

    if (debug)

        disp('this should break')

    end

break;

end

end

Nloc = find( sum( sum( Placeholder, 1), 2 ) )';

SymList = Placeholder(:,:,Nloc);

else

%Placeholder1 = zeros(dimens(1),dimens(2),4);
%Placeholder2 = Placeholder1;

Placeholder1 = PH1;
Placeholder2 = PH2;

%for PH1

for j = 1 : 3

    Inset = false(1,4);

    loc = false(1,4 - j);
    
        for i = j : 3
        
            loc(i-j+1) = isequal(Placeholder1(:,:,j),Placeholder1(:,:,i+1));
        
        end
    
    Inset( j + 1 : 4 ) = loc;

    tempLog = find ( Inset );

    if (debug)
    
        disp('remove duplicates')

    end

    Placeholder1(:,:,tempLog) = zeros(dimens(1),dimens(2),length(tempLog));
    
    Sloc = find( sum( sum( Placeholder1(:,:,(j:end)), 1 ), 2 ) );
    
    LSloc = length(Sloc);

    if (debug)

    disp('consolidate')

    end

    Placeholder1(:,:,j:(j+(LSloc-1))) = Placeholder1(:,:,(Sloc + (j-1)));

    if (debug)

    disp('zeros')

    end

    Placeholder1(:,:,(j+LSloc):end) = zeros(dimens(1),dimens(2),5-(j+LSloc));


tripSum = sum(sum(sum(Placeholder1(:,:,(j+1):end),1),2),3) == zeros(1,4-j);

if ((isequal(Placeholder1(:,:,j+1),zeros(dimens(1),dimens(2)))) && (isequal(tripSum,true(1,length(tripSum)))))

    if (debug)
    
    disp('this should break')

    end
    break;

end

end

%for PH2

for j = 1 : 3

    Inset = false(1,4);

    loc = false(1,4 - j);
    
        for i = j : 3
        
            loc(i-j+1) = isequal(Placeholder2(:,:,j),Placeholder2(:,:,i+1));
        
        end
    
    Inset( j + 1 : 4 ) = loc;

    tempLog = find ( Inset );

    if (debug)
    
        disp('remove duplicates')

    end

    Placeholder2(:,:,tempLog) = zeros(dimens(2),dimens(1),length(tempLog));
    
    Sloc = find( sum( sum( Placeholder2(:,:,(j:end)), 1 ), 2 ) );
    
    LSloc = length(Sloc);

    if (debug)

    disp('consolidate')

    end

    Placeholder2(:,:,j:(j+(LSloc-1))) = Placeholder2(:,:,(Sloc + (j-1)));

    if (debug)

    disp('zeros')

    end

    Placeholder2(:,:,(j+LSloc):end) = zeros(dimens(2),dimens(1),5-(j+LSloc));


tripSum = sum(sum(sum(Placeholder2(:,:,(j+1):end),1),2),3) == zeros(1,4-j);

if ((isequal(Placeholder2(:,:,j+1),zeros(dimens(2),dimens(1)))) && (isequal(tripSum,true(1,length(tripSum)))))

    if (debug)

    disp('this should break')

    end
    break;

end

end

Nloc1 = find( sum( sum( Placeholder1, 1), 2 ) )';
Nloc2 = find( sum( sum( Placeholder2, 1), 2 ) )';

L1 = length(Nloc1);
L2 = length(Nloc2);

Len = L1+L2;

big = max(dimens(1),dimens(2));

SymList = zeros(big,big,Len);

SymList(1:dimens(1),1:dimens(2),1:L1) = Placeholder1(:,:,Nloc1);
SymList(1:dimens(2),1:dimens(1),(L1+1):end) = Placeholder2(:,:,Nloc2);

end

end