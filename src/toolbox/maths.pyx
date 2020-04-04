
'''_____Standard imports_____'''
import numpy as np
cimport numpy as cnp

ctypedef cnp.cdouble_t CDTYPE_t
ctypedef cnp.double_t DTYPE_t
ctypedef double complex complex128_t


cpdef hilbert(cnp.ndarray[DTYPE_t, ndim=1] spectra):

    cdef complex128_t[1024] temp

    temp = np.fft.fft(np.array(spectra))

    temp[0: len(temp)//2] = 0

    return np.fft.fft(temp)


cpdef unwrap_phase(cnp.ndarray[DTYPE_t, ndim=1] spectra):


    cdef cnp.ndarray[cnp.cdouble_t, ndim=1] temp

    temp = hilbert(spectra)

    temp = np.angle( temp )

    temp = np.unwrap( temp )

    temp[0] = np.float64(0)

    return temp


cpdef apodization(cnp.ndarray[DTYPE_t, ndim=1] spectra):

    hanning = np.hanning( len(spectra) )

    spectra = hanning *  spectra

    return spectra


cpdef spectra2aline(cnp.ndarray[DTYPE_t, ndim=1] spectra):

    cdef cnp.ndarray[cnp.cdouble_t, ndim=1] ctemp

    ctemp = np.fft.fft(spectra)

    ctemp = np.fft.fftshift( ctemp )

    return np.abs( ctemp )