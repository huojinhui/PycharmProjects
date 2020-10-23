// 修改于 2019-03-06
function shellSort(arr) {
    varlen = arr.length;
    for(vargap = Math.floor(len / 2); gap > 0; gap = Math.floor(gap / 2)) {
        // 注意：这里和动图演示的不一样，动图是分组执行，实际操作是多个分组交替执行
        for(vari = gap; i < len; i++) {
            varj = i;
            varcurrent = arr[i];
            while(j - gap >= 0 && current < arr[j - gap]) {
                 arr[j] = arr[j - gap];
                 j = j - gap;
            }
            arr[j] = current;
        }
    }
    returnarr;
}