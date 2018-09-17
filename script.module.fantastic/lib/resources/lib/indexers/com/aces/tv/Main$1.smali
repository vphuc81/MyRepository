.class Lcom/aces/tv/Main$1;
.super Ljava/lang/Object;
.source "Main.java"

# interfaces
.implements Ljava/lang/Runnable;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/aces/tv/Main;->setVideoViewSurfaceRect(IIII)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/aces/tv/Main;

.field final synthetic val$bottom:I

.field final synthetic val$left:I

.field final synthetic val$right:I

.field final synthetic val$top:I


# direct methods
.method constructor <init>(Lcom/aces/tv;IIII)V
    .locals 0

    .prologue
    .line 58
    iput-object p1, p0, Lcom/aces/tv/Main$1;->this$0:Lorg/xbmc/kodi/Main;

    iput p2, p0, Lcom/aces/tv/Main$1;->val$left:I

    iput p3, p0, Lcom/aces/tv/Main$1;->val$top:I

    iput p4, p0, Lcom/aces/tv/Main$1;->val$right:I

    iput p5, p0, Lcom/aces/tv/Main$1;->val$bottom:I

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .locals 6

    .prologue
    .line 62
    new-instance v0, Landroid/widget/RelativeLayout$LayoutParams;

    iget-object v1, p0, Lcom/aces/tv/Main$1;->this$0:Lorg/xbmc/kodi/Main;

    invoke-static {v1}, Lcom/aces/tv/Main;->access$000(Lorg/xbmc/kodi/Main;)Lorg/xbmc/kodi/XBMCVideoView;

    move-result-object v1

    invoke-virtual {v1}, Lorg/xbmc/kodi/XBMCVideoView/XBMCVideoView;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    invoke-direct {v0, v1}, Landroid/widget/RelativeLayout$LayoutParams;-><init>(Landroid/view/ViewGroup$LayoutParams;)V

    .line 63
    iget v1, p0, Lcom/aces/tv/Main$1;->val$left:I

    iget v2, p0, Lcom/aces/tv/Main$1;->val$top:I

    iget-object v3, p0, Lcom/aces/tv/Main$1;->this$0:Lorg/xbmc/kodi/Main;

    invoke-static {v3}, Lcom/aces/tv/Main;->access$100(Lorg/xbmc/kodi/Main;)Landroid/widget/RelativeLayout;

    move-result-object v3

    invoke-virtual {v3}, Landroid/widget/RelativeLayout;->getWidth()I

    move-result v3

    iget v4, p0, Lcom/aces/tv/Main$1;->val$right:I

    sub-int/2addr v3, v4

    iget-object v4, p0, Lcom/aces/tv/Main$1;->this$0:Lorg/xbmc/kodi/Main;

    invoke-static {v4}, Lcom/aces/tv/Main;->access$100(Lorg/xbmc/kodi/Main;)Landroid/widget/RelativeLayout;

    move-result-object v4

    invoke-virtual {v4}, Landroid/widget/RelativeLayout;->getHeight()I

    move-result v4

    iget v5, p0, Lcom/aces/tv/Main$1;->val$bottom:I

    sub-int/2addr v4, v5

    invoke-virtual {v0, v1, v2, v3, v4}, Landroid/widget/RelativeLayout$LayoutParams;->setMargins(IIII)V

    .line 64
    iget-object v1, p0, Lcom/aces/tv/Main$1;->this$0:Lorg/xbmc/kodi/Main;

    invoke-static {v1}, Lcom/aces/tv/Main;->access$000(Lorg/xbmc/kodi/Main;)Lorg/xbmc/kodi/XBMCVideoView;

    move-result-object v1

    invoke-virtual {v1, v0}, Lorg/xbmc/kodi/XBMCVideoView;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    .line 65
    iget-object v0, p0, Lcom/aces/tv/Main$1;->this$0:Lorg/xbmc/kodi/Main;

    invoke-static {v0}, Lcom/aces/tv/Main;->access$000(Lorg/xbmc/kodi/Main;)Lorg/xbmc/kodi/XBMCVideoView;

    move-result-object v0

    invoke-virtual {v0}, Lorg/xbmc/kodi/XBMCVideoView;->requestLayout()V

    .line 66
    return-void
.end method
