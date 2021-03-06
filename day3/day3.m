%% PARSE INPUTS
current_dir = fileparts(mfilename('fullpath'));
fp = [current_dir '\input.txt'];
fid = fopen(fp);
textData = textscan(fid, '%n%n%n%n%n');
fclose(fid);
tableData = array2table([textData{:}], 'VariableNames', {'ID','XOFFSET','YOFFSET','WIDTH','HEIGHT'});
maxWidth = max(tableData.XOFFSET+tableData.WIDTH+1);
maxHeight = max(tableData.YOFFSET+tableData.HEIGHT+1);
fabricArray = zeros(maxWidth, maxHeight);
for i = 1:height(tableData)
    xIndexes = tableData.XOFFSET(i) + 1 : tableData.XOFFSET(i) + tableData.WIDTH(i);
    yIndexes = tableData.YOFFSET(i) + 1 : tableData.YOFFSET(i) + tableData.HEIGHT(i);
    fabricArray(xIndexes, yIndexes) = fabricArray(xIndexes, yIndexes) + 1;
end
answer1 = sum(sum(fabricArray > 1));
fprintf('The answer to part 1 is %i\n',answer1);

%% Part 2
for i = 1:height(tableData)
    xIndexes = tableData.XOFFSET(i) + 1 : tableData.XOFFSET(i) + tableData.WIDTH(i);
    yIndexes = tableData.YOFFSET(i) + 1 : tableData.YOFFSET(i) + tableData.HEIGHT(i);
    if sum(sum(fabricArray(xIndexes, yIndexes))) == length(xIndexes) * length(yIndexes)
        tableData(i,:)
    end
end

