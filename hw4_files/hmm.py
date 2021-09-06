import numpy as np
def forward(A, B, pi, O):
    """
    Calculates the probability of an observation sequence O given the model(A, B, pi).
    :param A: state transition probabilities (NxN)
    :param B: observation probabilites (NxM)
    :param pi: initial state probabilities (N)
    :param O: sequence of observations(T) where observations are just indices for the columns of B (0-indexed)
        N is the number of states,
        M is the number of possible observations, and
        T is the sequence length.
    :return: The probability of the observation sequence and the calculated alphas in the Trellis diagram with shape
             (N, T) which should be a numpy array.
    """
    Os=O.shape[0]
    As=A.shape[0]
    alpha=np.zeros((Os,As))
    alpha[0,:]=pi*B[:,O[0]]    
    for i in range(1,Os):
        for j in range(As):
            alpha[i][j]=alpha[i-1].dot(A[:,j])*B[j,O[i]]
    transposed=np.transpose(alpha)
    p=np.sum(transposed[:,Os-1])
    return (p,transposed)

def viterbi(A, B, pi, O):
    """
    Calculates the most likely state sequence given model(A, B, pi) and observation sequence.
    :param A: state transition probabilities (NxN)
    :param B: observation probabilites (NxM)
    :param pi: initial state probabilities(N)
    :param O: sequence of observations(T) where observations are just indices for the columns of B (0-indexed)
        N is the number of states,
        M is the number of possible observations, and
        T is the sequence length.
    :return: The most likely state sequence with shape (T,) and the calculated deltas in the Trellis diagram with shape
             (N, T). They should be numpy arrays.
    """
    Os=O.shape[0]
    As=A.shape[0]
    viterbi=np.zeros((As,Os))
    viterbi[:,0]=pi*B[:,O[0]]
    backtrackmatrix=np.zeros((As,Os))
    for i in range(1,Os):
        for j in range(As):
            temp=viterbi[:,i-1]*(A[:,j])*(B[j,O[i]])
            viterbi[j,i]=np.max(temp)
            backtrackmatrix[j,i]=np.argmax(temp)
    S=np.zeros(Os)
    last=int(np.argmax(viterbi[:,Os-1]))
    S[0]=last
    backtrackindex=1
    for i in range(Os-1,0,-1):
        S[backtrackindex]=backtrackmatrix[int(last),i]
        last=backtrackmatrix[int(last),i]
        backtrackindex+=1
    return (np.flip(S),viterbi)
