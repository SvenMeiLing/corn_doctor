<template>
	
	<div>
		
		<NGrid cols="2 s:3 m:4 l:5 xl:6 2xl:6" responsive="screen">
			
			<NGridItem>
				
				<div class="green">
					
					cols="2 s:3 m:4 l:5 xl:6 2xl:6" 默认2列 s宽度的时候是3列 m宽度的时候是4列 l的时候是5列 xl的时候是6列
					2xl是6列 不过需要 responsive=screen
					
					sss
				
				</div>
			
			
			</NGridItem>
			
			<NGridItem>
				
				<div class="light-blue" style="flex-direction:column">
					
					<div>
						
						2 还是 responsive=screen好用
					
					</div>
					
					<div>
						
						aa
					
					</div>
				
				
				</div>
			
			</NGridItem>
			
			<NGridItem>
				
				<div class="green">
					
					3
				
				</div>
			
			
			</NGridItem>
			
			<NGridItem>
				
				<div class="light-blue">
					
					4
				
				</div>
			
			</NGridItem>
			
			<NGridItem>
				
				<div class="green">
					
					5
				
				</div>
			
			
			</NGridItem>
			
			<NGridItem>
				
				<div class="light-blue">
					
					6
				
				</div>
			
			</NGridItem>
			
			<NGridItem>
				
				<div class="green">
					
					7
				
				</div>
			
			
			</NGridItem>
			
			<NGridItem>
				
				<div class="light-blue">
					
					8
				
				</div>
			
			</NGridItem>
		
		
		</NGrid>
		
		<hr>
		<!--<n-grid cols="4" item-responsive>-->
		<!--	-->
		<!--	<n-grid-item span="0 600:1 600:2 800:3">-->
		<!--		-->
		<!--		<div class="light-green">-->
		<!--			-->
		<!--			0～400px：不显示<br>-->
		<!--			-->
		<!--			400～600px：占据空间 1<br>-->
		<!--			-->
		<!--			600～800px：占据空间 2<br>-->
		<!--			-->
		<!--			800px 以上：占据空间 3-->
		<!--		-->
		<!--		</div>-->
		<!--	-->
		<!--	</n-grid-item>-->
		<!--	-->
		<!--	<n-grid-item>-->
		<!--		-->
		<!--		<div class="green">-->
		<!--			-->
		<!--			2-->
		<!--		-->
		<!--		</div>-->
		<!--	-->
		<!--	</n-grid-item>-->
		
		<!--</n-grid>-->
	
	
	</div>


</template>


<script setup lang="ts">
	
	import {NGrid, NGridItem} from 'naive-ui';


</script>


<style scoped>
	
	.light-green {
		
		height: 108px;
		
		background-color: rgba(0, 128, 0, 0.12);
		
		display: flex;
		
		align-items: center;
		
		justify-content: center;
		
	}
	
	.light-blue {
		
		width: 100%;
		
		height: 120px;
		
		background: #e923e9;
		
		display: flex;
		
		align-items: center;
		
		justify-content: center;
		
	}
	
	.green {
		
		height: 120px;
		
		background-color: rgba(0, 128, 0, 0.24);
		
		display: flex;
		
		align-items: center;
		
		justify-content: center;
		
	}

</style>
