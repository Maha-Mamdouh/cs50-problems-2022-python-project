from random import sample
import sys
import pyfiglet

def main():
    #first step: choose LeveL: lines 9:18
    print('Available Level>>>        1:Easy       2:Medium       0:close')
    while True:
        try:
            level=int(input('Level: ').strip())
            if level in [0,1,2]:
                break
            else:
                print('Wrong level. Choose again or 0 to close')
        except:
            print('Wrong level. Choose again or 0 to close')
    if level==0:
        sys.exit()
    # Second step: Create two matrix
    # 1st matrix :the visual one using fun:visual_mat
    # 2nd matrix:the matrix of values using fun:hidden_mat
    if level==1:
        print('               Easy Level')
        length=9
        mines=10
    elif level==2:
        print('                               Medium Level')
        length=16
        mines=40
    A=visual_mat(length)


    matrix_print(A)
    #matrix_print(mat)
    e=remaining_cells(A)
    q=0
    p=0
    #print(e)
    #third step: change matrix A accorind to ur choice in while loop

    #For the first time: we have to make sure the player won't choose a mine
    while True:
        try:
            I=input('choose row and column: ')
            if I=='':
                p=1
            else:
                row,col=list(map(int,I.strip().split()))
                tries=set()
                row-=1
                col-=1
        except:
            print('wrong choice please try again or enter to exit')
            continue
        if p==1:
            sys.exit()
        if not (0<=row<length and 0<=col<length):
            print('wrong choice please try again or enter to exit')
            continue
        tries.add((row,col))
        first_loc=length*(row)+col+1
        #print(first_loc)
        all_loc=[i for i in range(1,length**2+1)]
        all_loc.remove(first_loc)
        loc=sample(all_loc,mines)
        mat=hidden_mat(length,loc)

        if mat[row][col] in [k for k in range(1,length+1)]:
            A[row+1][col+1]=' '+str(mat[row][col])+' '
        else:
            A[row+1][col+1]='   '
            #print(look_around(mat,row,col))
            old_locations=look_around(mat,row,col)
            # print((row,col))
            # print(old_locations)
            n=1
            while n:
                new_location=set()
                for point in old_locations:
                    #print(point)
                    x,y=point
                    if mat[x][y] in [k for k in range(1,length+1)]:
                        A[x+1][y+1]=' '+str(mat[x][y])+' '
                    else:
                        #print(point)
                        A[x+1][y+1]='   '
                        new_location.update(look_around(mat,x,y))
                        #print(new_location)
                location=old_locations.union(new_location)
                n=len(location)-len(old_locations)
                old_locations=location.copy()
        matrix_print(A)
        e=remaining_cells(A)
        break

    # now the rest of game but we can select mine as well
    while e!=mines:
        try:
            I=input('choose row and column: ')
            if I=='':
                p=1
            else:
                row,col=list(map(int,I.strip().split()))
                tries=set()
                row-=1
                col-=1
        except:
            print('wrong choice please try again or enter to exit')
            continue
        if p==1:
            sys.exit()
        if not (0<=row<length and 0<=col<length):
            print('wrong choice please try again or enter to exit')
            continue
        if (row,col) in tries:
            print('already chosen')
            continue
        tries.add((row,col))
        if mat[row][col]=='x':
            q=1
            result = pyfiglet.figlet_format("Boom",font='doom')
            print(result)
            for i in range(length):
                for j in range(length):
                    if mat[i][j]=='x': A[i+1][j+1]='💥 '
            matrix_print(A)
            print('\nbetter luck next time\n')
            break
        elif mat[row][col] in [k for k in range(1,length+1)]:
            A[row+1][col+1]=' '+str(mat[row][col])+' '
        else:
            A[row+1][col+1]='   '
            #print(look_around(mat,row,col))
            old_locations=look_around(mat,row,col)
            # print((row,col))
            # print(old_locations)
            n=1
            while n:
                new_location=set()
                for point in old_locations:
                    #print(point)
                    x,y=point
                    if mat[x][y] in [k for k in range(1,length+1)]:
                        A[x+1][y+1]=' '+str(mat[x][y])+' '
                    else:
                        #print(point)
                        A[x+1][y+1]='   '
                        new_location.update(look_around(mat,x,y))
                        #print(new_location)
                location=old_locations.union(new_location)
                n=len(location)-len(old_locations)
                old_locations=location.copy()
        matrix_print(A)
        e=remaining_cells(A)
    if e==mines:
        result = pyfiglet.figlet_format("Congratulation",font='big')
        print(result)
#other functions
def remaining_cells(A):
    s=0
    for r in A:
        for c in r:
            if '⬜' in str(c): s+=1
    return s

def matrix_print(A):
    #for printing matrix each time
    for r in A:
        for c in r:
            print(c,end = " ")
        print()

def visual_mat(length):
    #format matrix for different digital
    if length<10:
        #a_in=[str(j)+' ' for j in range(1,length+1)]
        a_out=[f' {j} ' for j in range(1,length+1)]
        a_in=['⬜ ' for j in range(1,length+1)]
        A=[['_',*a_out,'_']]
        for i in range(1,length+1):
            A.append([str(i),*a_in,str(i)])
        A.append(['_',*a_out,'_'])
    else:
        a_out=[f' {j} ' for j in range(1,10)]
        c_in=[f'{j} ' for j in range(10,length+1)]
        a_in=['⬜ ' for j in range(1,length+1)]
        A=[['__',*a_out,*c_in,'__']]
        for i in range(1,10):
            A.append([' '+str(i),*a_in,str(i)])
        for i in range(10,length+1):
            A.append([str(i),*a_in,str(i)])
        A.append(['__',*a_out,*c_in,'__'])
    return A

def hidden_mat(length,loc):
    #generate locations for mines
    #loc=sample([i for i in range(1,length**2+1)],mines)
    #removed this line before calling method to be able to use unit test
    Mine_loc=[[(n-1)//length,(n-1)%length] for n in loc]

    mat=[]
    for i in range(length):
        mat.append([0 for j in range(length)])

    for mine in Mine_loc:
        #print(mine)
        i=mine[0]
        j=mine[1]
        mat[i][j]='x'
        neighbor=look_around(mat,i,j)
        for cell in neighbor:
            x,y=cell
            if mat[x][y]!='x': mat[x][y]+=1
    return mat

def look_around(mat,i,j):
    #function to look around for neighbor cells
    L=len(mat)-1
    if i not in range(L+1) or j not in range(L+1):
        raise IndexError()
    if i==0 and j==0:
        B=[(i,j+1),(i+1,j),(i+1,j+1)]
    elif i==0 and j==L:
        B=[(i,j-1),(i+1,j),(i+1,j-1)]
    elif i==0:
        B=[(i,j-1),(i,j+1),(i+1,j),(i+1,j-1),(i+1,j+1)]
    elif j==0 and i!=L:
        B=[(i+1,j),(i-1,j),(i-1,j+1),(i,j+1),(i+1,j+1)]
    elif j==0 and i==L:
        B=[(i-1,j),(i-1,j+1),(i,j+1)]
    elif i==L and j!=L:
        B=[(i,j-1),(i,j+1),(i-1,j-1),(i-1,j),(i-1,j+1)]
    elif i==L and j==L:
        B=[(i,j-1),(i-1,j-1),(i-1,j)]
    elif j==L:
        B=[(i-1,j-1),(i-1,j),(i,j-1),(i+1,j-1),(i+1,j)]
    else:
        B=[(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
    return set(B)

if __name__ == "__main__":
    main()