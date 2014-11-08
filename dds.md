Bo Haglund, Bob Richardson

Rev V, 2014-10-14

Latest DLL issue with this description is available at http://www.bahnhof.se/wb758135/

# Description of the DLL functions supported in Double Dummy Problem Solver 2.7
## Callable functions
The callable functions are all preceded with `extern "C" __declspec(dllimport) int __stdcall`.  The prototypes are available in `dll.h`. 
Return codes are given at the end.

Not all functions are present in all versions of the DLL.  For historical reasons, the function names are not entirely consistent with respect to the input format.  Functions accepting binary deals will end on Bin, and those accepting PBN deals will end on PBN in the future.  At some point existing function names may be changed as well, so use the new names!

## The Basic Functions

The basic functions `SolveBoard` and `SolveBoardPBN` solve each a single hand and are thread-safe, making it possible to use them for solving several hands in parallel. The other callable functions use the SolveBoard functions either directly or indirectly.

### The Multi-Thread Double Dummy Solver Functions

The double dummy trick values for all 5 * 4 = 20 possible combinations of a hand’s trump strain and declarer hand alternatives are solved by a single call to one of the functions `CalcDDtable` and `CalcDDtablePBN`. Threads are allocated per strain.

To obtain better utilization of available threads, the double dummy (DD) tables can be grouped using one of the functions `CalcAllTables` and `CalcAllTablesPBN`.

Solving hands can be done much more quickly using one of the multi-thread alternatives for calling SolveBoard. Then a number of hands are grouped for a single call to one of the functions `SolveAllChunksBin` and `SolveAllChunksPBN`.  The hands are then solved in parallel using the available threads.

The number of threads is automatically configured by DDS, taking into account the number of processor cores and available memory.  The number of threads can be influenced using the call `SetMaxThreads`.

The call `FreeMemory` causes DDS to give up its dynamically allocated memory.

### The PAR Calculation Functions

The PAR calculation functions find the optimal contract(s) assuming open cards and optimal bidding from both sides. In very rare cases it matters which side or hand that starts the bidding, i.e. which side or hand that is first to bid its optimal contract.

Two alternatives are given:

1. The PAR scores / contracts are calculated separately for each side. In almost all cases the results will be identical for both sides, but in rare cases the result is dependent on which side that “starts the bidding”, i.e. that first finds the bid that is most beneficial for the own side. One example is when both sides can make 1 NT.
2. The dealer hand is assumed to “start the bidding”. 

The presentation of the par score and contracts are given in alternative formats.

The functions `Par`, `SidesPar` and `DealerPar` do the par calculation; their call must be preceded by a function call calculating the double dummy table values.

The functions `SidesParBin` and `DealerParBin` provide binary output of the par results, making it easy to tailor-make the output text format. Two such functions, `ConvertToSidesTextFormat` and `ConvertToDealerTextFormat`, are included as examples. 

It is possible as an option to perform par calculation in `CalcAllTables` and `CalcAllTablesPBN`. 

The par calculation is executed using a single thread. But the calculation is very fast and its duration is negligible compared to the double dummy calculation duration.

### Double Dummy Value Analyser Functions

The functions `AnalysePlayBin`, `AnalysePlayPBN`, `AnalyseAllPlaysBin` and `AnalyseAllPlaysPBN` take the played cards in a game or games and calculate and present their double dummy values.

-------------------------------------------------------------------
Function | Arguments | Format | Comment |
-------------------------------------------------------------------
| `SolveBoard` | struct deal dl | Binary | The most basic function, |
|              | int target      |        | solves a single hand from  |
|              | int solutions    |        | the beginning or from |
|              | int mode          |        | later play           |
|              | struct futureTricks *futp | |                       |
|              | int threadIndex | Binary |   |                      |
| `SolveBoardPBN` | struct dealPBN dlPBN | PBN | As SolveBoard, but with |
|                 | int target |               | PBN deal format.     |
|                 | int solutions |            |                      |
|                 | int mode |                 |                      |
|                 | struct futureTricks *futp | |                     |
|                 | int threadIndex |          |                      |
------------------------------------------------------------------------
